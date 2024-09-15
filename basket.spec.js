describe('Sweet Shop Basket Tests', () => {
    beforeEach(() => {
        cy.visit('https://sweetshop.netlify.app/');
    });

    it('Add different quantities of at least 4 products in the basket and navigate to basket page', () => {
        // Add products to the basket
        cy.get('[data-cy="product-1"]').click();
        cy.get('[data-cy="product-quantity-1"]').clear().type('2');
        cy.get('[data-cy="add-to-basket-1"]').click();

        cy.get('[data-cy="product-2"]').click();
        cy.get('[data-cy="product-quantity-2"]').clear().type('1');
        cy.get('[data-cy="add-to-basket-2"]').click();

        cy.get('[data-cy="product-3"]').click();
        cy.get('[data-cy="product-quantity-3"]').clear().type('3');
        cy.get('[data-cy="add-to-basket-3"]').click();

        cy.get('[data-cy="product-4"]').click();
        cy.get('[data-cy="product-quantity-4"]').clear().type('2');
        cy.get('[data-cy="add-to-basket-4"]').click();

        // Navigate to basket page
        cy.get('[data-cy="view-basket"]').click();
    });

    it('Verify all selected items are present in the basket', () => {
        cy.get('[data-cy="basket-item-1"]').should('exist');
        cy.get('[data-cy="basket-item-2"]').should('exist');
        cy.get('[data-cy="basket-item-3"]').should('exist');
        cy.get('[data-cy="basket-item-4"]').should('exist');
    });

    it('Verify the total price in GBP is correct', () => {
        const prices = [10, 20, 15, 30]; // Example prices
        const quantities = [2, 1, 3, 2];
        let totalPrice = 0;

        prices.forEach((price, index) => {
            totalPrice += price * quantities[index];
        });

        cy.get('[data-cy="total-price"]').should('contain', totalPrice.toFixed(2));
    });

    it('Change the delivery type to Standard Shipping and verify the total price', () => {
        cy.get('[data-cy="delivery-type"]').select('Standard Shipping');
        const deliveryCost = 5; // Example delivery cost
        let totalPrice = 0;

        const prices = [10, 20, 15, 30]; // Example prices
        const quantities = [2, 1, 3, 2];

        prices.forEach((price, index) => {
            totalPrice += price * quantities[index];
        });

        totalPrice += deliveryCost;

        cy.get('[data-cy="total-price"]').should('contain', totalPrice.toFixed(2));
    });

    it('Fill the details and click on checkout', () => {
        cy.get('[data-cy="name"]').type('John Doe');
        cy.get('[data-cy="email"]').type('john.doe@example.com');
        cy.get('[data-cy="address"]').type('123 Sweet St, Candyland');
        cy.get('[data-cy="checkout"]').click();
    });
});
