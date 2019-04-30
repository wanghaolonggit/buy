<?php
set_time_limit(0);
$phones = require "./conf.php";
//目标url
$url = 'https://www.giftu.top/Qt/PigF/PiPointment?OID=345a578021a241eab07e7863934bc94d';
//post查询条件
$fields = 'OID=345a578021a241eab07e7863934bc94d';
$curl = curl_init();
curl_setopt_array($curl, array(
    CURLOPT_TIMEOUT => 60,
    CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
    CURLOPT_CUSTOMREQUEST => "POST",
    CURLOPT_HTTPHEADER =>  [
        "connection: keep-alive",
        "content-type: text/html",
        'X-Requested-With: XMLHttpRequest',
        "pragma: no-cache",
        "referer: https://www.giftu.top/PluginView/Qt/phone/1/index.html",
        "user-agent: Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
    ],
));
curl_setopt($curl, CURLOPT_URL, $url);
curl_setopt($curl, CURLOPT_POSTFIELDS, $fields);


foreach ($phones as $phone){
    curl_setopt ($curl, CURLOPT_COOKIE, $phone['cookies']);
    $httpcode = curl_getinfo($curl, CURLINFO_HTTP_CODE);

    $response = curl_exec($curl);
    var_dump($response);
}
