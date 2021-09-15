import handleResponseFromAPI from './2-then';

const promise = Promise.resolve();
console.log('🚀 value', handleResponseFromAPI(promise));
handleResponseFromAPI(promise).then((e) => console.log(e));
