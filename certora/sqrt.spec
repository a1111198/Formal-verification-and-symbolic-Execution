  methods{
    function sqrt(uint256 x) external returns uint256 envfree;
     function solmateSqrt(uint256 x) external returns uint256 envfree;
     function uniSqrt(uint256 y) external returns uint256 envfree;
     function sqrtUpperHalf(uint256 x) external returns uint256 envfree;
     function solmateUpperHalf(uint256 x) external returns uint256 envfree; 
  }
// invariant sqrtUni(uint256 x)
//     sqrt(x)==uniSqrt(x);
// invariant sqrtSol(uint256 x)
//     sqrt(x)==solmateSqrt(x);
rule sqrtSolHalf(uint256 x){
require(x!=0xfffffeffffffffffffffffffffffffffffffffffffffff);
assert(sqrtUpperHalf(x)==solmateUpperHalf(x));
}
