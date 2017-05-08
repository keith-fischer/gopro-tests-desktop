qgoproapp.showTestMessage("Testing ... starting...");
safeQuery(".GoProUILoginBypass").trigger("click"); // Switch to Media Browser
window.GoProApp.publish('userOpenMedia', { 'gumi': '92fce4d635c42e7ddf360ffde598faaf' }); // Open Media in Player
safeQuery(".GoProUIPlayerBackButton").trigger("click"); // Back to Media Browser
//qgoproapp.quitApp();
