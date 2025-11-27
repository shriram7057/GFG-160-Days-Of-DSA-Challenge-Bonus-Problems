/**
 * @param {number[]} arr
 * @returns {string}
 */
class Solution {
    minSum(arr) {
        // code here
        arr.sort((a,b)=> a - b);
        
        let a="";
        let b="";
        
        for(let i=0;i<arr.length;i++)
        {
            if(i%2===0) a+=arr[i];
            else b+= arr[i];
        }
        return this.addStrings(a,b);
    }
    addStrings(s1,s2){
        let i=s1.length-1;
        let j = s2.length-1;
        let carry=0;
        let res="";
    while(i>=0 || j>=0 || carry > 0)
    {
        const x=i>=0 ? s1[i]-'0':0;
        const y=j>=0 ? s2[j]- '0':0;
        
        const sum=x+y+carry;
        res=(sum%10)+res;
        carry=Math.floor(sum/10);
        i--;
        j--;
    }
    res=res.replace(/^0+/,'');
    return res === '' ? '0' : res;
    }
}
