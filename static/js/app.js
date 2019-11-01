

function allowDrop(ev) {
  ev.preventDefault();
}

function drag(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
}

function drop(id,ev) {
  ev.preventDefault();
  var ans = ev.dataTransfer.getData("text");
  ev.target.appendChild(document.getElementById(ans));
  alert(ans);
    $.ajax({
        url: "/ajax/test/",
        type: "GET",
        data: {
            ans : ans
        },
        success: function () {
            alert("ajax works");
            return true
        }
    });
    return false;
}