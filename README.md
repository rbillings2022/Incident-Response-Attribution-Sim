# Incident-Response-Attribution-Sim
- Scenario — On April 19th, 2023 at 12:50PM an employee at Boring Office sent their an email to everyone within the company. This employee claims that someone else at the company is impersonating them, and now we need to find who the rogue user is.
- Objective — correlating network layer (pcap/SMTP), DHCP lease logs, and Windows Security event logs to attribute a network action to a specific user account.
- Tools — pyshark (tshark wrapper), plaintext DHCP/Security log parsing.
- How to run — pip install pyshark, then python src/trace_sender.py.
- Sample output —
<img width="1623" height="463" alt="image" src="https://github.com/user-attachments/assets/841e38d3-4609-42a8-a28e-65c8a1f65e35" />

- What this demonstrates — 
  1. multi-source log correlation
  2. IOC pivoting (IP → host → user)
  3. basic DFIR workflow. 
Limitations / next steps —  it's a synthetic dataset, and that a real investigation would need timestamp-window validation, chain-of-custody logging, etc. This shows you understand where the toy project ends and real DFIR begins — reviewers like seeing that self-awareness.
