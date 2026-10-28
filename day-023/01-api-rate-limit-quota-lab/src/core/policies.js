export const defaultPolicy=Object.freeze({limit:5,windowMs:10000});
export const policyExamples=[
 {name:"Starter / bursty client",limit:5,windowMs:10000,notes:"Small burst budget over 10 seconds."},
 {name:"Service integration",limit:25,windowMs:60000,notes:"Moderate request allowance per minute."},
 {name:"Batch pipeline",limit:100,windowMs:60000,notes:"Higher volume; queueing and retry budgets still matter."}
];
