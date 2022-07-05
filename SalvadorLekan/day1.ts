function twoSum(nums: number[], target: number): [number, number] {
  const result: [number, number] = [0, 0];
  const map = new Map<number, number>();
  for (let i = 0; i < nums.length; i++) {
    const diff = target - nums[i];
    if (map.has(diff)) {
      result[0] = i;
      result[1] = map.get(diff)!;
      console.log(result);
      return result;
    }
    map.set(nums[i], i);
  }
  return result;
}
