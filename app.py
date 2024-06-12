from flask import Flask, request, render_template
from solution import Solution

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    heights = list(map(int, request.form.get('heights').split(',')))
    solution = Solution()
    result = solution.maxArea(heights)
    return render_template('index.html', result=result, heights=heights)

if __name__ == '__main__':
    app.run(debug=True)
