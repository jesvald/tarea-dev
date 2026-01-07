from typing import List, Tuple, Dict
import json


def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:
    
    def solve (pw, ph, rw, rh):    

        num_x = rw // pw
        num_y = rh // ph
        total_principal = num_x * num_y

        sobrante_derecha_ancho = rw - (num_x * pw)
        sobrante_abajo_alto = rh - (num_y * ph)
        
        extra_derecha = 0
        if sobrante_derecha_ancho >= ph and rh >= pw:
            extra_derecha = (sobrante_derecha_ancho // ph) * (rh // pw)

        extra_abajo = 0
        if sobrante_abajo_alto >= pw and (num_x * pw) >= ph:
            extra_abajo = (sobrante_abajo_alto // pw) * (num_x * pw) // ph

        return total_principal + extra_derecha + extra_abajo

    opciona = solve(panel_width, panel_height, roof_width, roof_height)
    opcionb = solve(panel_height, panel_width, roof_width, roof_height)

    return max(opciona, opcionb)    

def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()
