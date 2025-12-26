import heapq

class TriageSystem:
    def __init__(self):
        self.queue = []
        self.counter = 0  
        self.priority_map = {
            "Emergência": 1,
            "Urgente": 2,
            "Rotina": 3
        }

    def add_patient(self, name: str, priority: str):
        if priority not in self.priority_map:
            raise ValueError("Prioridade inválida")

        priority_value = self.priority_map[priority]
        heapq.heappush(
            self.queue,
            (priority_value, self.counter, name, priority)
        )
        self.counter += 1
    def call_next_patient(self):
        if not self.queue:
            return None
        _, _, name, priority = heapq.heappop(self.queue)
        return name, priority
    def reset_system(self):
        self.queue.clear()
        self.counter = 0
