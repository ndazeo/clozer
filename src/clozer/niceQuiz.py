from .quiz import Quiz

script = """
    <script>
        document.querySelectorAll("span.probability input").forEach(input => {
            input.setAttribute("pattern", "(0|0\\\\.[0-9]+|1)");

        });
        document.querySelectorAll("span.integer input").forEach(input => {
            input.setAttribute("pattern", "-?[0-9]+");
        });
        document.querySelectorAll("span.decimal input").forEach(input => {
            input.setAttribute("pattern", "-?[0-9]+(\\\\.[0-9]+)?");
        });
        document.querySelectorAll("span.optional input").forEach(input => {
            let pattern = input.getAttribute("pattern");
            input.setAttribute("pattern", pattern + "|NO");
        });
        document.querySelectorAll("span.inf input").forEach(input => {
            let pattern = input.getAttribute("pattern");
            input.setAttribute("pattern", pattern + "|INF");
        });

        var style = document.createElement('style');
        style.innerHTML = `
        #clozer_main input:invalid{
            background-color:#EE9090;
        }
        #clozer_main {
            background-color: white;
            padding: 10px;
        }
        span.underline input {
            border: none;
            border-bottom: 1px solid black;
            height: 1em;
        }
        .note{
            font-family: serif;
            font-size: 0.8em;
        }
        `;

        document.querySelector("#clozer_main").appendChild(style);
    </script>
"""

class NiceQuiz(Quiz):
    def preParse(self, txt):
        return f"""
<div id="clozer_main">
    {super().preParse(txt)}
    {script}
</div>
"""