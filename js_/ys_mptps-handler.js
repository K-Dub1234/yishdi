// ys_mptps-handler
// Mandatory Ping Transfer Protocol Secure (MPTPS)
pingID = Math.floor(Math.random() * 1.001);
var pings = {from:101, to:101, ID:pingID};
// 101 is the standard port number.
var trnsdata = pings.from * pings.to;
window.alert('mptps://ping.js.ys');