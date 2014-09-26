/**
 * Created by itachi on 9/24/14.
 */
$(document).ready(function () {

    // Create jqxExpander.
    $("#sign_in").jqxExpander({  toggleMode: 'none', width: '550px', showArrow: false, theme: 'metro' });
    // Create jqxInput.
    $("#username").jqxInput({  width: '300px', height: '30px', theme: 'metro', placeHolder:'اسم المستخدم' });
    // Create jqxPasswordInput.
    $("#password").jqxPasswordInput({  width: '300px', height: '30px', theme: 'metro', placeHolder:'كلمة المرور' });
    // Create jqxButton.
    $("#submit").jqxButton({ theme: 'metro', height: '30px', width: '300px' });
    // Create jqxValidator.
    $("#form").jqxValidator({
        rules: [
            { input: "#username", message: "مطلوب اسم المستخدم", action: 'keyup, blur', rule: 'required' },
            { input: "#password", message: "مطلوب كلمة المرور", action: 'keyup, blur', rule: 'required' }
        ], hintType: "label"
    });
    // Validate the Form.
    $("#submit").click(function () {
        $('#form').jqxValidator('validate');
    });
    // Update the jqxExpander's content if the validation is successful.
    $('#form').on('validationSuccess', function (event) {

        makeRequest("sign_in", [], {
            type: 'POST',
            data: {
                username: $("#username").jqxInput('val'),
                password: $("#password").jqxPasswordInput('val')
            },
            success: function (data) {
                if (data.success == "qa") window.location = "qa_view";
                else if (data.success == "camp") window.location = "camp_view";
                else if (data.success == "executive") window.location = "executive_view";
            }
        });

    });

});