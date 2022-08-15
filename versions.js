arr = window.location.href.split('/');
page = arr[arr.length - 1];
document.write('\
<dl>\
    <dt>Versions</dt> \
    <dd><a href="../master/' + page + '">master</a></dd>\
    <dd><a href="../109/' + page + '">110</a></dd>\
    <dd><a href="../109/' + page + '">109</a></dd>\
    <dd><a href="../106/' + page + '">106</a></dd>\
    <dd><a href="../104/' + page + '">104</a></dd>\
    <dd><a href="../103/' + page + '">103</a></dd>\
</dl>\
');