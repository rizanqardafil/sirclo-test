const { calculatePerbedaan } = require('./weightUtils');

describe('Weight Utils', () => {
  it('should calculate the correct perbedaan', () => {
    const weight1 = { max: 50, min: 49 };
    const weight2 = { max: 49, min: 47 };
    const perbedaan1 = calculatePerbedaan(weight1);
    const perbedaan2 = calculatePerbedaan(weight2);
    expect(perbedaan1).toBe(1);
    expect(perbedaan2).toBe(2);
  });
});
