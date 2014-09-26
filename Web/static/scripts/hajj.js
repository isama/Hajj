/**
 * Created by itachi on 9/23/14.
 */
/**
 * Created by itachi on 9/24/14.
 */
$(document).ready(function(){

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", GLOBAL_CSRF_TOKEN);
            }
        }
    });

    $("#errMessageNotification").jqxNotification({
        width: 250, position: "top-right", opacity: 0.9,
        autoOpen: false, animationOpenDelay: 800, autoClose: true,
        autoCloseDelay: 3000, template: "error"
    });

    $("#infoMessageNotification").jqxNotification({
        width: 250, position: "top-right", opacity: 0.9,
        autoOpen: false, animationOpenDelay: 800, autoClose: true,
        autoCloseDelay: 3000, template: "info"
    });

});

function makeRequest(method, params, options) {

    if (options.data == undefined) options.data = {};

    if (params.length > 0) {
        for (var i = 0; i < params.length; i++) {
            method += params[i] + "/"
        }
        method = method.substring(0, method.length - 1);
    }

    $.ajax({
        url : method,
        type : options["type"],
        contentType : "application/json; charset=utf-8",
        dataType : "json",
        data : JSON.stringify(options["data"])
    }).done(function(data) {
        if (data.error == undefined) {
            if (options.success)
                options.success(data);
            else {
                $("#infoMessageNotificationText").text(data.success);
                $("#infoMessageNotification").jqxNotification("open");
            }
        } else {
            if (options.error) {
                options.error(data);
            } else {
                // SHOW ERROR IN NOTIFICATION
                $("#errMessageNotificationText").text(data.error);
                $("#errMessageNotification").jqxNotification("open");
            }
        }
    });

}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

var GLOBAL_CSRF_TOKEN = getCookie('csrftoken');