from typing import List, Tuple, Dict
import json


def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:
    
    max_panels_width = 0

    for w,h in [(panel_width, panel_height), (panel_height, panel_width)]:
        if w > roof_width or h > roof_height:
            continue

        nx, ny = roof_width // w, roof_height // h
        total = nx * ny

        sobrante_x = roof_width - (nx * w)
        sobrante_y = roof_height - (ny * h)

        extra_x = sobrante_x // h * (roof_height // w) if sobrante_x >= h and roof_height >= w else 0

        extra_y = sobrante_y // w * (roof_width // h) if sobrante_y >= w and roof_width >= h else 0

        max_panels_width = max(max_panels_width, total + extra_x + extra_y)

    return max_panels_width


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
