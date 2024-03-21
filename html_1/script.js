const cardContainer = document.getElementById('card-container');
            const cards = document.querySelectorAll('.card');
            let currentCardIndex = 0;

            function like() {
                swipeCard('right');
            }

            function dislike() {
                swipeCard('left');
            }

            function swipeCard(direction) {
                cards[currentCardIndex].style.transform = `translate${direction === 'right' ? 'X' : 'Y'}(-100%) rotate(${direction === 'right' ? 15 : -15}deg)`;

                currentCardIndex++;

                if (currentCardIndex < cards.length) {
                    cards[currentCardIndex].style.transform = 'translate(0) rotate(0)';
                } else {
                    // Add logic for when there are no more cards
                    console.log('No more cards');
                }
            }