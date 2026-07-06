CHAPTER 7

# Defining Reliable, Safe, and Trustworthy Systems

W<sup>hile</sup> <sup>machine</sup> <sup>autonomy</sup> <sup>remains</sup> <sup>a</sup> <sup>popular</sup> <sup>goal,</sup> <sup>the</sup> <sup>goal</sup> <sup>of</sup> <sup>hu-</sup>man autonomy should remain equally strong in designers’ minds. man autonomy should remain equally strong in designers' minds. Machine and human autonomy are both valuable in certain contexts, but a combined strategy uses automation when it is reliable and human control when it is necessary. To guide design improvements it will be helpful to focus on the attributes that make HCAI systems reliable, safe, and trustworthy. These terms are complex, but I choose to define them with four levels of recommendations (see Part 4): (1) reliable systems based on sound software engineering practices, (2) safety culture through business management strategies, (3) trustworthy certification by independent oversight, and (4) regulation by government bodies.

These four communities are eager to accelerate development of reliable, safe, and trustworthy systems. Software engineers, business managers, independent oversight committees, and government regulators all care about the three goals, but I suggest practices that each community might be most efective in supporting.

Reliable<sup>1</sup> systems produce expected responses when needed. Reliability comes from appropriate technical practices for software engineering teams (Chapter 19). When failures occur, investigators can review detailed audit trails, much like the logs of flight data recorders, which have been so efective in civil aviation. The technical practices that support human responsibility, fairness, and explainability include:

• Audit trails and analysis tools

• Software engineering workflows

• Verification and validation testing

• Bias testing to enhance fairness

• Explainable user interfaces

Ample testing of software and analyses of training data used in machine learning promotes fairness. Explainability comes from many design features, but I focus on visual user interfaces that prevent or reduce the need for explainability. Cultures of safety<sup>2</sup> are created by managers who focus on these strategies (Chapter 20):

• Leadership commitment to safety

• Hiring and training oriented to safety

• Extensive reporting of failures and near misses

• Internal review boards for problems and future plans

• Alignment with industry standard practices

These strategies guide continuous refinement of training, operational practices, and root-cause failure analyses. In software engineering communities, the thirty-five-year-old Capability Maturity Models, developed by the Software Engineering Institute at Carnegie Mellon University, help team managers in applying the practices that support safety.<sup>3</sup> Managers can work to move their organization up through five levels of maturity, which are marked by increasingly consistent policies and measurement strategies that lead to increased software quality. The Capability Maturity Models are not perfect, but they remain in use, especially for military projects and cybersecurity.

Trustworthy systems are discussed more frequently than ever, but there is a long history of discussions to define trust. An influential contribution was political scientist Francis Fukuyama’s book Trust: The Social Virtues and the Creation of Prosperity, which focused on social trust “within a community of regular, honest, and cooperative behavior, based on commonly shared norms, on the part of the members of that community.”<sup>4</sup> He focused on human communities, but there are lessons for design of trust in technology.

However, public expectations go beyond trust or trusted systems; users want trustworthy systems. A system could be mistakenly trusted, but a trustworthy system is one that deserves trust, even though stakeholders struggle to measure that attribute. I take the position that trustworthiness is assessed by respected independent oversight. Since most consumers do not have the skill and cannot invest the efort to assess the trustworthiness of a system, they rely on established organizations, such as Consumer’s Report or Underwriters Laboratory. If a respected accounting firm, insurance company, or consumer advocacy group gives its seal of approval to a product or service, then consumers are likely to see it as trustworthy. The list of independent oversight organizations (Chapter 21) includes:

• Accounting firms conducting external audits

• Insurance companies compensating for failures

• Non-governmental and civil society organizations

• Professional organizations and research institutes

Government intervention and regulation also play an important role as protectors of the public interest, especially when large corporations elevate their agendas above the needs of residents and citizens (Chapter 22). Governments can encourage innovation as much as they can limit it, so learning from successes and failures will help policy-makers to make better decisions.

I chose to focus on reliable, safe, and trustworthy to simplify the discussion, but the rich literature on these topics advocates other attributes of systems, their performance, and user perceptions (Figure 7.1). These twenty-five attributes are all dificult to measure and resistant even to basic assessments, such as whether design changes would increase or decrease these attributes. Still, these are the attributes that are frequently used in discussions and ethical, responsible, or humane AI. Chapter 25 deals with the dificult issue of assessment.

Users of mature technologies such as elevators, cameras, home appliances, or medical devices know when these devices are reliable, safe, and trustworthy. They appreciate the high levels of automation but think of themselves as operating these devices in ways that give them control so as to accomplish their goals. Designers who adopt the HCAI mindset will emphasize strategies for enabling diverse users to steer, operate, and control their highly automated devices, while inviting users to exercise their creativity to refine designs. Well-designed automation can ensure finer human control, such as in surgical robots that enable surgeons to make precise incisions in dificult to reach organs.

Successful technologies enable humans to work in interdisciplinary teams so as to coordinate and collaborate with managers, peers, and subordinates. Since humans are responsible for the actions of the technologies they use, they are more likely to adopt technologies that show current status on a control panel, provide users with a mental model to predict future actions, and allow users to stop actions that they can’t understand. Well-designed user interfaces provide vital support for human activities in ways that reduce workload, raise performance, and increase safety. The special cases requiring fully automatic action or fully human control demand additional design review, as discussed in Chapter 8.

![](images/9e105b31525466055a850d2f63da68c75a8b1f80ed15225324ebcc11c10c7ecb.jpg)  
Fig 7.1 Some of the many attributes proposed as goals for HCAI systems.

Designers of reliable, safe, and trustworthy systems will also promote resilience, clarify responsibility, increase quality, and encourage creativity.<sup>5</sup> Human creativity is needed to extend existing designs, come up with wholly new approaches, and coordinate collaboration when needed to deal with unanticipated problems. Still broader goals are to ensure privacy, increase cybersecurity, support social justice, and protect the environment.

The HCAI framework (Chapter 8) guides designers and researchers to consider new possibilities that advance reliable, safe, and trustworthy systems. After all, most consumers, industrial supervisors, physicians, and airplane pilots are not interested in computer autonomy; what they want are systems to increase their performance dramatically, while simplifying their efort, so they can devote themselves to their higher aspirations. The HCAI framework shows how careful design leads to computer applications that enable high levels of human control while also providing high levels of automation.