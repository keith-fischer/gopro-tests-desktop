class Dashing.List extends Dashing.Widget
	ready: ->
	if @get('unordered')
		$(@node).find('ol').remove()
	else
		$(@node).find('ul').remove()
##########################################
		
	onData: (data) ->
		if data and data.items and data.items.length>0
			listlen=99
			if data.items.length>listlen
				n=data.items.length-listlen
				for i in [1..n]
					data.items.splice(i,1)
			data
		#data.items[0].gp_pass="data.items="+data.items.length


#newrow=data.items[data.items.length]

#debugger=true
#console.log(data)
#data[0].gp_pass="!!!"
#data
#      p = newrow.gp_pass
#	  f=newrow.gp_fail
#	  nt=newrow.gp_nottest
#	  t=p+f+nt
#	  pp=(p/t)*100
#	  fp=(f/t)*100
#	  tp=(nt/t)*100
#	  newrow.gp_pass=pp+"%"
#	  newrow.gp_fail=fp+"%"
#	  newrow.gp_nottest=tp+"%"
#data.items[data.items.length-1]=newrow
