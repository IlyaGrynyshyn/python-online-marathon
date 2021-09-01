function mapCreator(keys, values) {
   let map = new Map();
   let i = 0;
   for (let value of values) {
        if (typeof value == "string") {
               map.set(keys[i], value)
           }
           i++
   }
   return map
}

const map = mapCreator([1, 2, 3, 4, 5, 6, 7],["Lviv", "Rivne", "Kyiv", "Dnipro", "Kharkiv", "Chernivtsi", "Ivano-Frankivsk"]);
console.log(map.get(1));
