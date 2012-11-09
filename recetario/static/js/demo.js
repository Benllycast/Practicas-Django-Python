$(function(){
	$('#menu a[href*='+location.pathname.split("/")[1]+'][class != activo]').addClass('activo');
});