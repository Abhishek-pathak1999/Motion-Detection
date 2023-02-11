var area1=$('.res_area');
var area2=$('.res_area div');
var hand = $(".hand");
var head=$(".head");
area2.on('mouseenter',function(e){
	head.css({transform: "rotate(0deg)"})
	head.css({right: '-150px'})
	
	$('.hands').css({transform: "scale(1.8)"});
	$('.cursor').css('display','block')
	$('*').css('cursor','none')
	setTimeout(function(e){
		$('.hands').css({transform: "scale(1)"});
		
		hand.css('display','none')
		head.css('display','none')
	},200)
	setTimeout(function(e){
		$('*').css('cursor','default')
		$('.cursor').css('display','none')
		hand.css('display','block')
		head.css('display','block')
	},4000)
})
function angle(e){
	total_height=window.innerHeight
	total_width=window.innerWidth

	currentX=e.clientX
	currentY=e.clientY

	x=total_width-currentX
	y=total_height-currentY
	// rad=y/x
	tan=-(90-(Math.atan2(y,x)*180/Math.PI));
	return tan
}


area1.on('mousemove',function(e){
	hand.css({transform: "rotate(" + angle(e) + "deg)"});
	head.css({transform: "rotate(-10deg)"})
	head.css({right: '-70px'})
})
area1.on('mouseout',function(e){
	hand.css({transform: "rotate(0deg)"});
	head.css({transform: "rotate(0deg)"})
	head.css({right: '-150px'})
})