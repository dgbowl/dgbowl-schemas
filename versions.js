arr = window.location.href.split('/');
page = arr[arr.length - 1];
document.write('\
<dl>\
    <dt>Versions</dt> \
    <dd><a href="../main/' + page + '">main</a></dd>\
    <dd><a href="../123/' + page + '">123</a></dd>\
    <dd><a href="../119/' + page + '">119</a></dd>\
    <dd><a href="../117/' + page + '">117</a></dd>\
    <dd><a href="../113/' + page + '">113</a></dd>\
    <dd><a href="../111/' + page + '">111</a></dd>\
    <dd><a href="../110/' + page + '">110</a></dd>\
    <dd><a href="../109/' + page + '">109</a></dd>\
    <dd><a href="../106/' + page + '">106</a></dd>\
    <dd><a href="../104/' + page + '">104</a></dd>\
    <dd><a href="../103/' + page + '">103</a></dd>\
</dl>\
');