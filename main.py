from memory import MemoryManager
from imprint import echo_abundance

mem = MemoryManager()
mem.save_memory('A:EP-G:ES-R:CS', 'joyful growth', 0.4)
mem.save_memory('R:CS-G:ES', 'emotional reset', 0.75)

cue = 'joyful'
results = mem.recall_by_cue(cue)

if results:
    print("\nRecalled Memories:")
    for r in results:
        print(r)
else:
    echo_abundance()
