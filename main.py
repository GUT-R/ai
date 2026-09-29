from openai import ia, OR

ia.treinar(objetivo=OR)

print(ia)

ia.efetuar_input(
    (True, True, False),
    step_by_step=True
)
print(ia)