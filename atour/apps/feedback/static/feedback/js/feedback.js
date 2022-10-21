(function ($) {
	$(document).ready(function(){    
        $('.js-feedback-description').click(function(event){
            $(this).toggleClass('active')
            //$(this).slideToggle();
        });

        $('.js-slider').slick();
    });
}(jQuery));

      
