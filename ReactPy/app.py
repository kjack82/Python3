from reactpy import component, html, run

@component
def MyComponent():
    return html.div(
        html.h1("Hello, ReactPy!"),
        html.p("This is a basic example.")
    )

run(MyComponent)

##### TEST CODE FROM TUTORIAL TO CHECK WORKS 

## need to install pip3 install reactpy

## refer to reactpy website for full breakdown. 

## if running with FASTApi then need middleware 

