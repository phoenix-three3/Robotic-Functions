🎯 Robotic-Functions
I imagine that I work in Thoughtful’s robotic automation factory.
--------------------------------------------------------------------------------------------------------------------
1.📦 Package Sorter Robot Arm
A simple Python project for sorting packages in a robotic factory based on their **size** and **weight**. 🦾

2.🎯 Objective

Determine where a package should go:
- ✅ **STANDARD** – if it's **not bulky** and **not heavy**
- ⚠️ **SPECIAL** – if it's **bulky** or **heavy** (just one)
- ❌ **REJECTED** – if it's **both bulky and heavy**

3.📏 Rules
1) A package is **bulky** if:
- Volume (width × height × length) **≥ 1,000,000 cm³**  
  _or_  
- Any dimension **≥ 150 cm**

2) A package is **heavy** if:
- Mass **≥ 20 kg**

4.✅ How to Run
-Clone the repository
git clone https://github.com/your-username/package-sorter.git
cd package-sorter

-Make sure Python is installed
Run this in your terminal: python --version

-Run the script
In your terminal, navigate to the folder where sorter.py is saved and run: python main.py

5.🧠 How It Works

```python
def sort(width: int, height: int, length: int, mass: int) -> str:
    ...
