var s1 = Math.floor(Math.random() * 11), s2 = Math.floor(Math.random() * 11), s3 = Math.floor(Math.random() * 11), s4 = Math.floor(Math.random() * 11)
var toasterslots = [];

function setdata(sa, sb, sc, sd) {
	s1, s2, s3, s4 = sa, sb, sc, sd
	var toasterslots = [s1, s2, s3, s4];
	alert(toasterslots.toString());
}

setdata(1, 2, 3, 4)