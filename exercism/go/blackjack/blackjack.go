package blackjack

// ParseCard returns the integer value of a card following blackjack ruleset.
func ParseCard(card string) int {
	switch {
	case card == "ace":
		return 11
	case card == "two":
		return 2
	case card == "three":
		return 3
	case card == "four":
		return 4
	case card == "five":
		return 5
	case card == "six":
		return 6
	case card == "seven":
		return 7
	case card == "eight":
		return 8
	case card == "nine":
		return 9
	case card == "ten":
		return 10
	case card == "jack":
		return 10
	case card == "queen":
		return 10
	case card == "king":
		return 10
	default:
		return 0
	}
}

// FirstTurn returns the decision for the first turn, given two cards of the
// player and one card of the dealer.
func FirstTurn(card1, card2, dealerCard string) string {
	playerTotal := ParseCard(card1) + ParseCard(card2)
	dealerValue := ParseCard(dealerCard)

	// Rule 1: If both cards are "ace", always split.
	if card1 == "ace" && card2 == "ace" {
		return "P"
	}

	// Rule 2: If player has Blackjack (21 total)
	if playerTotal == 21 {
		if dealerValue == 10 || dealerValue == 11 { // dealer has a face card or ace
			return "S"
		}
		return "W" // Automatically win
	}

	// Rule 3: If total is between 17 and 20, always stand.
	if playerTotal >= 17 && playerTotal <= 20 {
		return "S"
	}

	// Rule 4: If total is between 12 and 16, stand unless dealer has 7 or higher.
	if playerTotal >= 12 && playerTotal <= 16 {
		if dealerValue >= 7 {
			return "H"
		}
		return "S"
	}

	// Rule 5: If total is 11 or lower, always hit.
	return "H"
}
