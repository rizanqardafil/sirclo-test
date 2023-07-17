const request = require('supertest');
const app = require('./app');

describe('Weight Tracker', () => {
  it('should return weight data with correct values', async () => {
    const response = await request(app).get('/');
    expect(response.status).toBe(200);
    expect(response.body).toHaveLength(5);
    expect(response.body[0].tanggal).toBe('2018-08-22');
    expect(response.body[0].max).toBe(50);
    expect(response.body[0].min).toBe(49);
  });

  it('should update weight data when edited', async () => {
    const response = await request(app)
      .post('/weight/edit/2018-08-18')
      .send({ max_weight: 55, min_weight: 48 });
    expect(response.status).toBe(302); // Assuming redirect status
    const updatedData = await request(app).get('/');
    const editedWeight = updatedData.body.find((w) => w.tanggal === '2018-08-18');
    expect(editedWeight.max).toBe(55);
    expect(editedWeight.min).toBe(48);
  });
});
