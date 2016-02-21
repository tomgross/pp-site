$(document).ready(function(){
  $(window).resize(function(){
    if($(window).width() >= 768){
      $('.clickable-dropdown').on('click', function(){
        window.location.href=$(this).attr('href');
      });
    }
  }).resize();
});
