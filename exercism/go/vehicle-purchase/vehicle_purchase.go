package purchase

import (
	"fmt"
	"strings"
)

// NeedsLicense determines whether a license is needed to drive a type of vehicle. Only "car" and "truck" require a license.
func NeedsLicense(kind string) bool {
	if kind == "car" {
		return true
	} else if kind == "truck" {
		return true
	} else {
		return false
	}		
}

// ChooseVehicle recommends a vehicle for selection. It always recommends the vehicle that comes first in lexicographical order.
func ChooseVehicle(option1, option2 string) string {
	if strings.Compare(option1, option2) < 0 {
		return fmt.Sprintf("%s is clearly the better choice.", option1)
	}
	return fmt.Sprintf("%s is clearly the better choice.", option2)
}

// CalculateResellPrice calculates how much a vehicle can resell for at a certain age.
func CalculateResellPrice(originalPrice float64, age float64) float64 {
	intAge := int(age)
	if intAge < 3 {
		return originalPrice * 0.8
	} else if intAge >= 3 && intAge < 10 {
		return originalPrice * 0.7
	} else {
		return originalPrice * 0.5
	}
}
