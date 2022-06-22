
(function ($) {
    "use strict";


    /*==================================================================
    [ Focus Contact2 ]*/
    $('.input2').each(function(){
        $(this).on('blur', function(){
            if($(this).val().trim() != "") {
                $(this).addClass('has-val');
            }
            else {
                $(this).removeClass('has-val');
            }
        })    
    })
            
  
    
    /*==================================================================
    [ Validate ]*/
    var LIMIT_BAL = $('.validate-input input[name="LIMIT_BAL"]');
    var sex = $('.validate-input input[name="sex"]');
    var Education = $('.validate-input input[name="Education"]');
    var Marriage = $('.validate-input input[name="Marriage"]');
    var Age = $('.validate-input input[name="Age"]');
    var pay0 = $('.validate-input input[name="pay0"]');
    var pay2 = $('.validate-input input[name="pay2"]');
    var pay3 = $('.validate-input input[name="pay3"]');
    var pay4 = $('.validate-input input[name="pay4"]');
    var pay5 = $('.validate-input input[name="pay5"]');
    var pay6 = $('.validate-input input[name="pay6"]');
    var bill1 = $('.validate-input input[name="bill1"]');
    var bill2 = $('.validate-input input[name="bill2"]');
    var bill3 = $('.validate-input input[name="bill3"]');
    var bill4 = $('.validate-input input[name="bill4"]');
    var bill5 = $('.validate-input input[name="bill5"]');
    var bill6 = $('.validate-input input[name="bill6"]');
    var payam1 = $('.validate-input input[name="payam1"]');
    var payam2 = $('.validate-input input[name="payam2"]');
    var payam3 = $('.validate-input input[name="payam3"]');
    var payam4 = $('.validate-input input[name="payam4"]');
    var payam5 = $('.validate-input input[name="payam5"]');
    var payam6 = $('.validate-input input[name="payam6"]');


    $('.validate-form').on('submit',function(){
        var check = true;

        if($(LIMIT_BAL).val().trim() == ''){
            showValidate(LIMIT_BAL);
            check=false;
        }

        if($(sex).val().trim() == ''){
            showValidate(sex);
            check=false;
        }

        if($(Education).val().trim() == ''){
            showValidate(Education);
            check=false;
        }

        if($(Marriage).val().trim() == ''){
            showValidate(Marriage);
            check=false;
        }

        if($(Age).val().trim() == ''){
            showValidate(Age);
            check=false;
        }

        if($(pay0).val().trim() == ''){
            showValidate(pay0);
            check=false;
        }



        if($(pay2).val().trim() == ''){
            showValidate(pay2);
            check=false;
        }

        if($(pay3).val().trim() == ''){
            showValidate(pay3);
            check=false;
        }

        if($(pay4).val().trim() == ''){
            showValidate(pay4);
            check=false;
        }

        if($(pay5).val().trim() == ''){
            showValidate(pay5);
            check=false;
        }

        if($(pay6).val().trim() == ''){
            showValidate(pay6);
            check=false;
        }

        if($(bill1).val().trim() == ''){
            showValidate(bill1);
            check=false;
        }

        if($(bill2).val().trim() == ''){
            showValidate(bill2);
            check=false;
        }

        if($(bill3).val().trim() == ''){
            showValidate(bill3);
            check=false;
        }

        if($(bill4).val().trim() == ''){
            showValidate(bill4);
            check=false;
        }

        if($(bill5).val().trim() == ''){
            showValidate(bill5);
            check=false;
        }

        if($(bill6).val().trim() == ''){
            showValidate(bill6);
            check=false;
        }

        if($(payam1).val().trim() == ''){
            showValidate(payam1);
            check=false;
        }

        if($(payam2).val().trim() == ''){
            showValidate(payam2);
            check=false;
        }

        if($(payam3).val().trim() == ''){
            showValidate(payam3);
            check=false;
        }

        if($(payam4).val().trim() == ''){
            showValidate(payam4);
            check=false;
        }

        if($(payam5).val().trim() == ''){
            showValidate(payam5);
            check=false;
        }

        if($(payam6).val().trim() == ''){
            showValidate(payam6);
            check=false;
        }

        return check;
    });


    $('.validate-form .input2').each(function(){
        $(this).focus(function(){
           hideValidate(this);
       });
    });

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
    
    

})(jQuery);