export function validatePolicy(policy){
 const errors=[];
 if(!policy||typeof policy!=="object"){return ["Policy must be an object."];}
 if(!Number.isInteger(Number(policy.limit))||Number(policy.limit)<1||Number(policy.limit)>1000)errors.push("Limit must be an integer from 1 to 1000.");
 if(!Number.isInteger(Number(policy.windowMs))||Number(policy.windowMs)<1000||Number(policy.windowMs)>3600000)errors.push("Window must be an integer from 1000 to 3600000 milliseconds.");
 return errors;
}
