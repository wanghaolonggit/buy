<?php
$phones = require "conf.php";
set_time_limit(0);
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

curl_setopt ($curl, CURLOPT_COOKIE, '__jsluid=7c3fcec438e425586fccec0c0302c0b0; 8AC3302B4D959C2160994B0E4F1D9412=1B1E3123332604BC; 6279D8D3C2C2B32346CF69B6581FBBB8=67B0A6284E3EA6AF25D7B919C60B5E7CCD170FB54B2A3427072CE4C397774F93291B28AC3352BBACC325EE038E4C7919F1F93781BBBF0F63; 3C936632BE4E76B9DD1E483C2EB2D500=71AF92B46E72412205B3E4451A876847A7FE42CB42E745EBB64B4B8F71DA44CE86FCCF0F9FCE64CE; 0BFE2B2D28B84A9623459C0A45F9C06A=9CCF54454CB2BC62B625DF9A4A93B393; __jsl_clearance=1556447888.233|0|TayiW4y84nOXIj5JQTok4vg46uY%3D');
//foreach ($phones as $phone){
//    curl_setopt ($curl, CURLOPT_COOKIE, $phone['cookies']);



    curl_setopt($curl, CURLOPT_URL, $url);
    //post fields
    curl_setopt($curl, CURLOPT_POSTFIELDS, $fields);
    $response = curl_exec($curl);
    $err = curl_error($curl);
    $httpcode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
    var_dump($response);
//}