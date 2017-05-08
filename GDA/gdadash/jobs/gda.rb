require 'uri'
require 'net/http'
require 'json'
require 'date'
require 'time'

def get_dashboard(ip)
  url = URI.parse("http://#{ip}/dashboard_testruns")
  http = Net::HTTP.new(url.host, url.port)
  #http.use_ssl = (url.scheme == 'https')
  #http.verify_mode = OpenSSL::SSL::VERIFY_NONE
  response = http.request(Net::HTTP::Get.new(url.request_uri))
  json = JSON.parse(response.body)
  return json
end

def get_testresults(path)
    # Read JSON from a file, iterate over objects
  if File.file?(path)
    file = open(path)
    json = file.read

    obj = JSON.parse(json)
    return obj
  end
  return nil
end

def evalreport(path)

    rptobj=get_testresults(path)
    if not rptobj or not rptobj.key?("summaryreport")
        return nil
    end
    sumrpt=rptobj["summaryreport"]
    if sumrpt.key?("title") and sumrpt.key?("passfail")
      return sumrpt
    end
    return nil
end

def seconds_between_dates(startdatetime,enddatetime)
  elapsed_seconds = ((enddatetime - startdatetime) * 24 * 60 * 60).to_i
  return elapsed_seconds
end

def datetime_elapse(startdatetime,enddatetime)
  t = seconds_between_dates(startdatetime,enddatetime)
  mm, ss = t.divmod(60)            #=> [4515, 21]
  hh, mm = mm.divmod(60)           #=> [75, 15]
  dd, hh = hh.divmod(24)           #=> [3, 3]
  
  elapse = "%d Days-%02d:%02d:%02d" % [dd, hh, mm, ss]
  #=> 3 days, 3 hours, 15 minutes and 21 seconds
  return elapse
end

def percentdone(total, completed)
  p = (completed/total) *100
  return "#{p.round(2).to_s}%"
end

def eeval(vvar = nil)
  svar = nil
  begin
    svar=vvar
    if svar != nil
      if defined? svar
        if svar.is_a?(Numeric)
          svar = svar.to_s
        end
        svar = svar.downcase.strip
      else
        return "***"
      end
    end
  rescue => e
    puts "ERROR:#{e}"
    svar = "###"
  end
  #puts svar
  return svar
end





#json -->            html mapping
#scenarios[10] e.g. pass1,pass2...pass10
#status              pass1,fail1,error1
#datetime            datetime1
#scenario            scenario1
#failstep            resultinfo1
def evalscenarios(scenarios)
  data={} # = { pass: pass, fail: fail, error: error, datetime: datetime1, resultinfo1: result1}
  count=0
  runstopped = nil
  latestdate =nil

  scenarios.each do |test|
    begin
      count +=1
      pf = eeval(test['status']) if test.has_key?('status')
      dt = eeval(test['datetime']) if test.has_key?('datetime')
      sc = eeval(test['scenario']) if test.has_key?('scenario')
      ff = eeval(test['failstep']) if test.has_key?('failstep')
      if pf
        if pf == "pass"
          data["pass#{count}"] = "PASS"
        elsif pf == "fail"
          data["fail#{count}"] = "FAIL"
        elsif pf == "error"
          data["error#{count}"] = "ERROR"
        end
        if dt
          #testdate = DateTime.parse(dt)
          #data["datetime#{count}"] = testdate.strftime("%F %T")
          starttime = Time.parse(dt).localtime
          dtlocal =starttime.strftime("%F %T")
          data["datetime#{count}"]=dtlocal
        end
        if sc
          data["scenario#{count}"] = sc
          puts "\t#{pf}:#{dt}-#{sc}"
        end
        if ff and pf != "pass"
          data["resultinfo#{count}"] = ff
        else
          data["resultinfo#{count}"] = ""
        end
      end
    rescue => e
      puts "ERROR scenarios.each do |test| SCENARIO:#{count}\n#{e}"
    end
  end
  return runstopped, latestdate, data
end


#json -->            html mapping
#runstatus           runstatusrun, runstatusstop, runstatusdone
#app                 runinfo
#appver              runinfo
#camera              runinfo
#camera_ver          runinfo
#mobile              runinfo
#mobile_os           runinfo
#scenario_count      runinfo
#reset_count         runinfo
#runid               runinfo
#host                host
#datetime_start      datetimestart
#duration            elapse
#passed              passed
#failed              failed
#errors              errors
#untested            untested
#                    pdone
#featurefile         featuref

def evaltestrun(dashrun)
  runid=nil
  run = {}
  begin
    runstopped=nil
    temp=nil
    latestdate=nil
    runstopped, latestdate, run=evalscenarios(dashrun['scenarios']) if dashrun.has_key?('scenarios')
    #puts run
    if run.has_key?('scenario1') # should have at least 1 scenario
      runstat = eeval(dashrun['runstatus']) if dashrun.has_key?('runstatus')
#      puts "#{runstat}<<<<<<<<<<<<<<<<<<<<<"
      if runstat
        if runstat == "running"
          run['runstatusrun']="RUNNING"
        elsif runstat == "stopped"
          run['runstatusstop']="STOPPED"
        elsif runstat == "done"
          run['runstatusdone']="DONE"
          runstopped = nil #overrides the timeout
        end
      end
#      if runstopped == "STOPPED"
#
#        run['runstatusstop']="STOPPED"
#        run['runstatusrun']=""
#        puts "run['runstatusstop']  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
#      end
      # runinfo
      runid = eeval(dashrun['runid']) if dashrun.has_key?('runid')
        run['runid']="RunID:#{runid.to_s}" if runid
#      puts runid
      testcount = 0

      #p=f=e=u =0
      temp = eeval(dashrun['passed']) if dashrun.has_key?('passed')
      p=temp.to_i if temp
      run['passed']="PASSED:#{temp.to_s}" if temp
      temp = eeval(dashrun['failed']) if dashrun.has_key?('failed')
      f=temp.to_i if temp
      run['failed']="FAILED:#{temp.to_s}" if f > 0
      run['failed0']="FAILED:#{temp.to_s}" if f==0
      temp = eeval(dashrun['errors']) if dashrun.has_key?('errors')
      e=temp.to_i if temp
      run['errors']="ERRORS:#{temp.to_s}" if e > 0
      run['errors0']="ERRORS:#{temp.to_s}" if e == 0
      temp = eeval(dashrun['untested']) if dashrun.has_key?('untested')
      u=temp.to_i if temp
      run['untested']="UNTESTED:#{temp.to_s}" if temp
      scenario_count = eeval(dashrun['run_scenario_count']) if dashrun.has_key?('run_scenario_count')
      testcount = scenario_count.to_i if scenario_count
      
      temp = eeval(dashrun['datetime_start']) if dashrun.has_key?('datetime_start')
      
      if temp
        #startdate = Date.parse(temp)
        starttime = Time.parse(temp).localtime
        dtlocal =starttime.strftime("%F %T")
        run['datetimestart']=dtlocal
      end
      
      temp = eeval(dashrun['duration']) if dashrun.has_key?('duration')
      run['elapse']=temp if temp
      
      temp = eeval(dashrun['percentdone']) if dashrun.has_key?('percentdone')
      run['pdone']=temp.to_s if temp
      
      temp = eeval(dashrun['featurefile']) if dashrun.has_key?('featurefile')
        
      run['featuref']=temp.to_s if temp
      
      temp = eeval(dashrun['host']) if dashrun.has_key?('host')
      run['host']=temp.to_s if temp
      runinfo = ""
      app = eeval(dashrun['app']) if dashrun.has_key?('app')
      runinfo += app if app
      appver = eeval(dashrun['appver']) if dashrun.has_key?('appver')
      runinfo += appver + "|" if appver
      camera = eeval(dashrun['camera']) if dashrun.has_key?('camera')
      runinfo += camera if camera
      camera_ver = eeval(dashrun['camera_ver']) if dashrun.has_key?('camera_ver')
      runinfo += camera_ver+"|" if camera_ver
      mobile = eeval(dashrun['mobile']) if dashrun.has_key?('mobile')
      runinfo += mobile if mobile
      mobile_os = eeval(dashrun['mobile_os']) if dashrun.has_key?('mobile_os')
      runinfo += mobile_os+"|" if mobile_os
      reset_count = eeval(dashrun['reset_count']) if dashrun.has_key?('reset_count')
      runinfo += " RelayCount:"+reset_count.to_s+"|" if reset_count

      runinfo += "TestCount:"+testcount.to_s+"|" if testcount
      run['runinfo']=runinfo.to_s if runinfo
    end
  rescue => e
    puts "ERROR RUN evaltestrun:#{runid}\n#{e}"
  end
  return run
end

def updatedash(reportpath)
  rows = []
  dashdata = evalreport(reportpath)
  dt = ""
  failinfo="None"
  title="not found"
  gdainfo = "Not found"
  if dashdata != nil and dashdata.length>0
    count=0
    begin
      if dashdata.key?("failinfo")
      	failinfo = "#{dashdata["failinfo"].to_s}"
      end
      if dashdata.key?("passfail")
      	gdainfo = "#{dashdata["passfail"].to_s}"
      end
      gdainfo = "#{gdainfo}  #{failinfo}"
      puts gdainfo
      if dashdata.key?("title")
      	title = "#{dashdata["title"].to_s}"
      end        
      puts "#{title} #{gdainfo} #{failinfo}"
      send_event('gdainfo', { text: gdainfo ,title: title })
    rescue => e
      puts "ERROR: #{e.to_s}"
    end
    p=f=e=u=t=0

    count+=1
    puts "#{count}=============================================================="
    #dashrun = evaltestrun(item)
    #rows.push(dashrun)
    #puts rows
    t = dashdata['songcount'].to_i
    p += dashdata['passed'].to_i
    f += dashdata['failed'].to_i
    e += dashdata['errors'].to_i
    u =t-(p+f) #total tests -(passed+failed)

    puts "t=#{t.to_s}"
    puts "p=#{p.to_s}"
    puts "f=#{f.to_s}"
    puts "e=#{e.to_s}"
    puts "u=#{u.to_s}"

    #t = p+f
    tt = t#t -(p+f)#t+u
    pc = ((t.to_f/tt.to_f) * 100).round(2)
    pp = ((p.to_f/tt.to_f) * 100).round(2)
    ff = ((f.to_f/tt.to_f) * 100).round(2)
    ee = ((e.to_f/tt.to_f) * 100).round(2)

    #puts "pc=#{pc.to_s}"
    puts "tt=#{tt.to_s}"
    if dashdata.key?('failedinfo')
      failedinfo= dashdata['failedinfo']
      failedinfo.each do |item|
        row={}
        dt=''
        png=''
        t15=''
        t30=''
        t60=''
        ld=''
        lt=''
        png=''
        row['gridtest'] = "Music Regression"
        if item.key?('lastdate')
          ld=item['lastdate'].to_s
        end
        if item.key?('lasttime')
          lt=item['lasttime'].to_s
        end
        row['griddatetime']=ld + " " + lt
        if item.key?('png')
          png=item['png']
          row['gridpng']=png
        end
        if item.key?('t60')
          t60=item['t60'].to_s
          row['t60']="60-#{t60}Sec"
        end
        if item.key?('t30')
          t30=item['t30'].to_s
          row['t30']="30-#{t30}Sec"
        end
        if item.key?('t15')
          t15=item['t15'].to_s
          row['t15']="15-#{t15}Sec"
        end
        if item.key?('title')
          row['gridsong']="\"#{item['title'].to_s}\""
        end
        if item.key?('FAILED')
          #row['runinfo'] += ' ' + item['FAILED'].to_s
          row['gridstatus'] = 'FAILED:'+item['FAILED'].to_s
        end


        rows.push(row)
      end
    end
    title2 = 'Test run still looking good!'
    if f>0 or e>0
      title2= "Song Tests Failed = #{f}, Script Errors = #{e}"
    end
    puts '=================================================='
    puts title
    puts title2
    puts gdainfo
    puts rows.to_s
    puts '=================================================='
    send_event('gda_graph1', { value: pp , title: "PASSED: #{p}", max: 100})
    send_event('gda_graph2', { value: ff , title: "FAILED: #{f}", max: 100})
    send_event('gda_graph3', { value: ee , title: "ERRORS #{e}", max: 100})
    send_event('gda_graph4', { value: pc , title: "TOTAL: #{tt}", max: 100})
    #begin
      send_event('gdalist', {items: rows,title: title2})
    #rescue => e
      puts e.to_s
    #end
  else
    puts "ERROR! No dashboard data"

    send_event('gdainfo', { text: "Dashboard data returned empty. The dashboard test results collection server is offline or empty." ,title: "ERROR! No dashboard data" })
    send_event('gda_graph1', { value: 0 , title: "PASSED 0", max: 100})
    send_event('gda_graph2', { value: 0 , title: "FAILED 0", max: 100})
    send_event('gda_graph3', { value: 0 , title: "ERRORS 0", max: 100})
    send_event('gda_graph4', { value: 0 , title: "TOTAL 0", max: 100})
    run = {}
    run['gridlabel']="Start Node server from terminal: node /path_to/gopro-tests-mobile/tools/nodeproj/dashboard_mgr/index.js"
    #rows.push(run)
    #run = {}
    run['gridvalue']="Any dashboard reporting issues please contact:  Keith Fischer"
    rows.push(run)
    send_event('gdalist', { items: rows , title: "NO DASHBOARD DATA"})
  end
end

SCHEDULER.every '20s', allow_overlapping: false do
  begin
    reportpath=File.join(ENV["HOME"],"gda_music_images","gda_create_tests_regression.json")
    #reportpath = "/Volumes/gda_music_images/gda_create_tests_regression.json"
    updatedash(reportpath)
  rescue => e
    puts e.to_s
  end
end
