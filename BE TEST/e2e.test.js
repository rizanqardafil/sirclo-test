describe('Weight Tracker', () => {
  it('should display the correct weight data on the index page', () => {
    cy.visit('/');
    cy.get('tbody tr').should('have.length', 5); // Assuming there are 5 weight data rows
    cy.contains('2018-08-18').should('exist');
  });

  it('should allow editing weight data', () => {
    cy.visit('/weight/edit/2018-08-18');
    cy.get('#max_weight').clear().type('55');
    cy.get('#min_weight').clear().type('48');
    cy.get('form').submit();
    cy.url().should('eq', 'http://localhost:5000/');
    cy.contains('2018-08-18').should('not.exist');
    cy.contains('55').should('exist');
    cy.contains('48').should('exist');
  });
});
