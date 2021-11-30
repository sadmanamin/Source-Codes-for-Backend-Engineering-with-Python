import http from 'k6/http';
import { check } from 'k6';
 
export let options = {
    // vus: 10,
    // duration: '30s',
    stages: [
        { duration: '5s', target: 50 },
        { duration: '10s', target: 500 },
        { duration: '5s', target: 500},
        {duration: '5s', target: 50},
	    {duration: '5s', target: 0},
	  // {duration: '5s',target: 0}
    ],
};
 
export default () => {
    var url = 'http://0.0.0.0:4001';
    let res = http.get(url);
    check(res, {
			'is status 200': (r) => r.status === 200,
		//	'body contains pong':(r) => r.body === 'hello from service2',
		});	
}

