$(document).ready(function(){
  $(window).resize(function(){
    if($(window).width() >= 992){
      $('.clickable-dropdown').on('click', function(){
        window.location.href=$(this).attr('href');
      });
    }
  }).resize();
});
