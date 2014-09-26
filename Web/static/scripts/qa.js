/**
 * Created by itachi on 9/25/14.
 */

$(document).ready(function () {

    $("#taskHeader").jqxExpander({  toggleMode: 'none', width: '604px', showArrow: false, theme: 'metro' });
    $("#sign_out").jqxButton({ theme: 'metro', height: '30px', width: '90px', template:'danger' });
    $(".normal-button").jqxToggleButton({ theme: 'metro', height: '40px', width: '90px'});
    $(".activity-status").each(function(index) {
        var status = (this.dataset.content == "False") ? 'danger' : 'success';
        var val =  (this.dataset.content == "False") ? 'لا' : 'نعم';
        $(this).jqxButton({ theme: 'metro', height: '40px', width: '50px', template:status });
        $(this).val(val);
    });
    $(".toggle-supervisor").jqxToggleButton({ theme: 'metro', height: '40px', width: '150px' });
    $(".toggle-task").jqxToggleButton({ theme: 'metro', height: '40px', width: '290px' });
    $(".comment-button").jqxButton({ theme: 'metro', height: '30px', width: '70px', template:'primary' });
    $(".comment-text").jqxInput({ placeHolder: "أدخل التعليق!", width: '590px', theme: 'metro' });
    $(".normal-button").click(function () {
        var divId = "comment-div-" + this.dataset.content;
        var toggled = $(this).jqxToggleButton('toggled');
        if (toggled) {
            $("#" + divId).css("display", "block");
        } else {
            $("#" + divId).css("display", "none");
        }
    });
    $(".comment-button").click(function () {
        var divId = "comment-div-" + this.dataset.content;
        var textArea = "comment-text-" + this.dataset.content;
        // NEED TO MAKE AJAX REQUEST
        var me = this;
        var activity_id = this.dataset.content;
        var val = $("#" + textArea).jqxInput('val');
        if (val != "") {
            makeRequest("log_action/", [activity_id], {
                type: 'POST',
                data: {
                    comment: $("#" + textArea).jqxInput('val')
                }
            });
            $("#comment-btn-" + activity_id).jqxToggleButton("toggle");
            $("#" + divId).css("display", "none");
        } else {
            $("#infoMessageNotificationText").text("Please enter a comment to save");
            $("#infoMessageNotification").jqxNotification("open");
        }

    });
    $("#sign_out").click(function () {
        makeRequest("sign_out", [], {
            type: 'GET',
            success: function (data) {
                window.location = '/hajj'
            }
        });
    });
    $(".activity-status").click(function () {
        // NEED TO MAKE AJAX REQUEST To Update Status
        var me = this;
        var activity_id = this.id.replace("status-", "");
        var status = (this.dataset.content == "False") ? 'True' : 'False';
        this.dataset.content = status;
        var val =  (this.dataset.content == "False") ? 'لا' : 'نعم';
        makeRequest("log_action/", [activity_id], {
            type: 'POST',
            data: {
                status: status
            },
            success: function (data) {
                $(me).jqxButton({
                    theme: 'metro', height: '40px', width: '50px',
                    template:(me.dataset.content == "False") ? 'danger' : 'success'
                });
                $(me).val(val);
            }
        });
    });
});
