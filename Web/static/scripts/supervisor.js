/**
 * Created by itachi on 9/25/14.
 */

$(document).ready(function () {

});

$("#supHeader").jqxExpander({  toggleMode: 'none', width: '604px', showArrow: false, theme: 'metro' });
$(".sup-normal-button").jqxToggleButton({ theme: 'metro', height: '40px', width: '90px'});
$(".sup-activity-status").each(function(index) {
    var status = (this.dataset.content == "False") ? 'danger' : 'success';
    var val =  (this.dataset.content == "False") ? 'لا' : 'نعم';
    $(this).jqxButton({ theme: 'metro', height: '40px', width: '50px', template:status });
    $(this).val(val);
});
$(".sup-toggle-task").jqxToggleButton({ theme: 'metro', height: '40px', width: '440px' });
$(".sup-comment-text").jqxInput({ width: '586px', theme: 'metro' });
$(".sup-normal-button").click(function () {
    var divId = "sup-comment-div-" + this.dataset.content;
    var toggled = $(this).jqxToggleButton('toggled');
    if (toggled) {
        $("#" + divId).css("display", "block");
    } else {
        $("#" + divId).css("display", "none");
    }
});
