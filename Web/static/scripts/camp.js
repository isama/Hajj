/**
 * Created by itachi on 9/25/14.
 */

$(document).ready(function () {

    $("#taskHeader").jqxExpander({  toggleMode: 'none', width: '604px', showArrow: false, theme: 'metro' });
    $("#sign_out").jqxButton({ theme: 'metro', height: '30px', width: '90px', template:'danger' });
    $("#sign_out").click(function () {
        makeRequest("sign_out", [], {
            type: 'GET',
            success: function (data) {
                window.location = '/hajj'
            }
        });
    });
    $(".supervisor-name").each(function(index) {
        var count = parseInt(this.dataset.count);
        if (count > 0) {
            $(this).jqxButton({ theme: 'metro', height: '25px', width: '180px', template:'danger' });
        } else {
            $(this).jqxButton({ theme: 'metro', height: '25px', width: '180px', template:'success' });
        }
    });
    $(".task-count").each(function(index) {
        var count = parseInt(this.dataset.count);
        if (count > 0) {
            $(this).jqxButton({ theme: 'metro', height: '80px', width: '180px', template:'danger' });
        } else {
            $(this).jqxButton({ theme: 'metro', height: '80px', width: '180px', template:'success' });
        }
    });
    $(".task-count").click(function() {
        var count = parseInt(this.dataset.count);
        var supervisor = this.dataset.content;
        makeRequest("supervisor_detail", [], {
            type: 'POST',
            data: {
                supervisor: supervisor,
                user: this.dataset.parent
            },
            success: function (data) {
                // GET HTTP RESPONSE HERE
                // SET THAT HTML IN SOME DIV
                $("#supervisorDetail").html(data.success);
            }
        });
    });
});
