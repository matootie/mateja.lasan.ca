(function() {
    var doc_ols = document.getElementsByTagName("ol");
    for (i = 0; i < doc_ols.length; i++) {
        var ol_start = doc_ols[i].getAttribute("start") - 1;
        doc_ols[i].setAttribute("style", "counter-reset:ol " + ol_start + ";");
    }
})();
