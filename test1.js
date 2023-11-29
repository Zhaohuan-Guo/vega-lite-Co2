const countryList = require('country-list');

// 将国家名称转换为国家缩写
const countryName = 'Hong Kong';
const countryCode = countryList.getCode(countryName);

console.log(countryCode); // 输出 "US"
