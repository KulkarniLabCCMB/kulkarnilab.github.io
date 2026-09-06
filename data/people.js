/* ============================================================================
   PEOPLE
   ----------------------------------------------------------------------------
   photo   filename inside assets/img/people/ — e.g. "pratik-khopkar.jpg"
           Leave "" and the card shows the person's initials instead.
   links   [{label, url}] — Scholar, ORCID, iNaturalist, personal site, etc.

   NOTE FOR SIDDHARTH: roles below were inferred from your CV and news page.
   Correct them here and they update across the whole site.
   ========================================================================== */

window.PI = {
  name: "Siddharth Kulkarni",
  role: "Principal Investigator",
  titles: [
    "ANRF Ramanujan Faculty Fellow, CSIR-Centre for Cellular and Molecular Biology",
    "Assistant Professor, Academy of Scientific and Innovative Research (AcSIR)"
  ],
  photo: "siddharth-kulkarni.jpg",
  bio: [
    "I am fascinated by biodiversity and by what keeps it going. My work asks why some branches of the tree of life are staggeringly diverse while their close relatives are not, using chelicerates \u2014 spiders, ticks, mites, scorpions, whip spiders, camel spiders and their kin \u2014 as the test case.",
    "Before starting the lab I completed a Ph.D. with Gustavo Hormiga at George Washington University on the spider tree of life and the miniature orb-weavers, and a postdoc with Prashant Sharma at the University of Wisconsin-Madison working on arachnid phylogenomics and genome architecture. Along the way I have described new species, new families and a chromosome-level genome or two.",
    "Outside the lab I coordinate SpiderIndia, a community science network of more than 8,000 people across South Asia who photograph and document spiders. Much of what we know about where Indian spiders actually live comes from them."
  ],
  links: [
    { label: "Google Scholar", url: "https://scholar.google.co.in/citations?user=xo9jTM0AAAAJ&hl=en" },
    { label: "ResearchGate", url: "https://www.researchgate.net/profile/Siddharth_Kulkarni6" },
    { label: "GitHub", url: "https://github.com/sskspider" }
  ]
};

window.GROUPS = [
  {
    id: "research-group",
    title: "Research group",
    blurb: "Doctoral students, project staff and research assistants based at LaCONES, CSIR-CCMB.",
    people: [
      {
        name: "Neel Ganguly", role: "Ph.D. student", since: "2026", photo: "",
        note: "Co-supervised doctoral research at CSIR-CCMB.", links: []
      },
      {
        name: "Shripad Manthen", role: "Spider taxonomist", since: "2026", photo: "",
        note: "The lab's in-house expert on spider identification and morphology.", links: []
      },
      {
        name: "Nithin K. A.", role: "Project Associate I", since: "2026", photo: "",
        note: "Genomics and computational work on chelicerate diversification.", links: []
      },
      {
        name: "Pratik Khopkar", role: "Project Associate I", since: "2025", photo: "",
        note: "Comparative genomics of Acari; genome erosion and gene family evolution.", links: []
      },
      {
        name: "Arjun Cherukutty", role: "Technical Assistant", since: "2025", photo: "",
        note: "Molecular laboratory work, library preparation and sequencing.", links: []
      },
      {
        name: "Dibyo Mazumder", role: "Research member", since: "2025", photo: "",
        note: "Acarine comparative genomics.", links: []
      }
    ]
  },
  {
    id: "students",
    title: "Students and visiting researchers",
    blurb: "Masters, dissertation and internship students working with the lab, including co-supervised students at IISER Thiruvananthapuram.",
    people: [
      {
        name: "Aakashkumar Pathak", role: "Ph.D. student, co-supervised", since: "2024", photo: "",
        note: "IISER Thiruvananthapuram.", links: []
      },
      {
        name: "Shreya Salunkhe", role: "Dissertation research trainee", since: "2025", photo: "",
        note: "CSIR-CCMB Dissertation Research Training Programme; from IISER Thiruvananthapuram.", links: []
      },
      {
        name: "Neha Tambe", role: "Research intern", since: "2026", photo: "",
        note: "D. Y. Patil University, Pune.", links: []
      },
      {
        name: "Rushikesh Mule", role: "BS-MS student", since: "2024", photo: "",
        note: "IISER Thiruvananthapuram. Acari phylogenomics.", links: []
      },
      {
        name: "Jyoti Bhoi", role: "BS-MS student", since: "2024", photo: "",
        note: "IISER Thiruvananthapuram. Ancient gene linkages in Acari.", links: []
      },
      {
        name: "Nishaad Savale", role: "BS-MS student", since: "2024", photo: "",
        note: "IISER Thiruvananthapuram. Ultraconserved elements in Acari.", links: []
      },
      {
        name: "Sweta Acharjya", role: "BS-MS student", since: "2024", photo: "",
        note: "IISER Thiruvananthapuram.", links: []
      }
    ]
  }
];

/* Past members and mentees. Shown as a simple list rather than cards. */
window.ALUMNI = [
  { name: "Meghana Balija", detail: "Summer Training Programme 2025, Sri Padmavati Mahila Visvavidyalayam, Tirupati \u2014 the first student in the lab" },
  { name: "Benjamin Klementz", detail: "University of Wisconsin-Madison, 2022\u20132023 \u2014 UCE library preparation and analysis" },
  { name: "Hugh Steiner", detail: "University of Wisconsin-Madison, 2022\u20132023 \u2014 UCE library preparation and analysis" },
  { name: "Brooke Pellegrini", detail: "George Washington University, 2019 \u2014 spider curation and identification" },
  { name: "Dheeraj Halali", detail: "Parvatibai Chowgule College, Goa, 2016 \u2014 remote mentoring" }
];
