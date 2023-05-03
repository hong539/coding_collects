import time

class TodoApp:
    def __init__(self):
        self.items = []
        self.text = ''
        self.handleChange = self.handleChange.bind(self)
        self.handleSubmit = self.handleSubmit.bind(self)

    def render(self):
        return """
        <div>
            <h3>TODO</h3>
            <TodoList items={self.items} />
            <form onSubmit={self.handleSubmit}>
                <label htmlFor="new-todo">
                    What needs to be done?
                </label>
                <input
                    id="new-todo"
                    onChange={self.handleChange}
                    value={self.text}
                />
                <button>
                    Add #{len(self.items) + 1}
                </button>
            </form>
        </div>
        """

    def handleChange(self, e):
        self.text = e.target.value

    def handleSubmit(self, e):
        e.preventDefault()
        if len(self.text) == 0:
            return
        newItem = {
            'text': self.text,
            'id': int(time.time())
        }
        self.items.append(newItem)
        self.text = ''

class TodoList:
    def __init__(self, items):
        self.items = items

    def render(self):
        return """
        <ul>
            {0}
        </ul>
        """.format(''.join(f'<li key={item["id"]}>{item["text"]}</li>' for item in self.items))

if __name__ == "__main__":
    # root.render(<TodoApp />)
    root = TodoApp()
    print(root.render())