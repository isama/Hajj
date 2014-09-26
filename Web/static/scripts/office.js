/**
 * Created by itachi on 9/25/14.
 */

$(document).ready(function () {

    $("#campHeader").jqxExpander({  toggleMode: 'none', width: '604px', showArrow: false, theme: 'metro' });
    $("#sign_out").jqxButton({ theme: 'metro', height: '30px', width: '90px', template:'danger' });
    $("#sign_out").click(function () {
        makeRequest("sign_out", [], {
            type: 'GET',
            success: function (data) {
                window.location = '/hajj'
            }
        });
    });
    $(".camp-name").each(function(index) {
        var count = parseInt(this.dataset.count);
        if (count > 0) {
            $(this).jqxButton({ theme: 'metro', height: '25px', width: '180px', template:'danger' });
        } else {
            $(this).jqxButton({ theme: 'metro', height: '25px', width: '180px', template:'success' });
        }
    });
    $(".camp-task-count").each(function(index) {
        var count = parseInt(this.dataset.count);
        if (count > 0) {
            $(this).jqxButton({ theme: 'metro', height: '80px', width: '180px', template:'danger' });
        } else {
            $(this).jqxButton({ theme: 'metro', height: '80px', width: '180px', template:'success' });
        }
    });
    $(".camp-task-count").click(function() {
        var user_id = this.dataset.content;
        makeRequest("camp_detail", [], {
            type: 'POST',
            data: {
                user: user_id,
                camp: this.name
            },
            success: function (data) {
                // GET HTTP RESPONSE HERE
                // SET THAT HTML IN SOME DIV
                $("#campDetail").html(data.success);
            }
        });
    });
});
