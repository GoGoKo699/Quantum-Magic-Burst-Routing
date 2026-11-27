# Project understanding map

The first twelve milestones build the shared vocabulary from an injected phase rotation to the fixed factory and its source-noise model. The remaining eighteen develop the source assignment, posterior decisions, phase-tied receivers, residual faults, and delivery costs. [Gottesman’s tutorial](GOTTESMAN_BRIDGE.md) supplies the educational background, and the [scientific account](../science/README.md) gives the exact statements and proofs.

| Phase | Milestones | Understanding gained |
|---|---|---|
| Background and preliminaries | [M01](#m01-the-t-state)–[M08](#m08-the-fifteen-input-labels) | Gate teleportation, check signs, and output parity |
| Background and preliminaries | [M09](#m09-the-first-undetected-slot-faults)–[M12](#m12-the-single-block-design-question) | Physical faults versus source events and the cost of rejection |
| Narrative and innovation | [M13](#m13-a-bundle-induces-one-check-column)–[M17](#m17-maximum-syndrome-information) | Constructive input assignment, fifth-order suppression, and maximal information |
| Narrative and innovation | [M18](#m18-correction-from-nonzero-records)–[M22](#m22-a-whole-burst-and-a-partial-pair) | Syndrome decisions and partial-burst limits |
| Narrative and innovation | [M23](#m23-independent-errors-on-top-of-bursts)–[M26](#m26-scheduling-the-same-circuit) | Exact residual-noise law and schedule comparisons |
| Narrative and innovation | [M27](#m27-more-check-wires)–[M30](#m30-the-complete-routing-argument) | Larger gadgets and synthesis |

## Phase I. Background and preliminaries

### M01 The T state

**Central question.** What resource lets the factory supply a non-Clifford gate?

**Understanding target.** Identify the T state as T applied to a plus state. Explain why it is prepared separately and why the orthogonal phase-flipped state represents a bad output in this model.

**Prerequisites.** None within this map.

**Conceptual connection.** Connect the quality of an ancilla state to the reliability of a later non-Clifford operation.

**Sources.** [Gottesman §4.5](GOTTESMAN_BRIDGE.md#read-the-parts-that-carry-the-argument) · [Factory model](../science/model.md)

### M02 Pauli conjugation

**Central question.** What happens to a Pauli fault when a Clifford gate follows it?

**Understanding target.** Track a preexisting Pauli through conjugation and distinguish its support from its overall phase.

**Prerequisites.** [M01](#m01-the-t-state).

**Conceptual connection.** Explain why the final effect of a fault depends on the gates between its location and measurement.

**Sources.** [Gottesman §3.5](GOTTESMAN_BRIDGE.md#read-the-parts-that-carry-the-argument) · [Factory model](../science/model.md)

### M03 Gate teleportation

**Central question.** How can an ancilla and a measurement replace a direct T application?

**Understanding target.** Describe the roles of ancilla, measurement outcome, and conditional correction. Relate Gottesman’s phase rotation notation to the T gate.

**Prerequisites.** [M01](#m01-the-t-state), [M02](#m02-pauli-conjugation).

**Conceptual connection.** Follow where a bad input can enter a circuit whose Clifford operations are ideal.

**Sources.** [Gottesman §4.5](GOTTESMAN_BRIDGE.md#read-the-parts-that-carry-the-argument) · [Factory model](../science/model.md)

### M04 The injection fault rule

**Central question.** What does a raw Z error do after injection into a parity rotation?

**Understanding target.** Follow the two cases of the injection measurement and account for the intended conditional correction. Describe the residual Pauli associated with the faulty rotation.

**Prerequisites.** [M02](#m02-pauli-conjugation), [M03](#m03-gate-teleportation).

**Conceptual connection.** Distinguish a misplaced quantum state from a slot-specific fault on the factory’s circuit wires.

**Sources.** [Factory model](../science/model.md)

### M05 Check signs as syndrome bits

**Central question.** What error information survives measurement of the check wires?

**Understanding target.** Use Pauli commutation to interpret a sign flip. Encode the four check signs relative to the ideal run as a binary vector.

**Prerequisites.** [M02](#m02-pauli-conjugation), [M04](#m04-the-injection-fault-rule).

**Conceptual connection.** Connect an X readout of a check wire to the Z support of the residual Pauli on that wire.

**Sources.** [Gottesman §2.3](GOTTESMAN_BRIDGE.md#read-the-parts-that-carry-the-argument) · [Factory model](../science/model.md)

### M06 Binary check columns

**Central question.** How does the syndrome of one slot determine the syndrome of a set of slots?

**Understanding target.** Assign each injection a column of the binary check matrix. Add columns over the binary field to follow simultaneous faults.

**Prerequisites.** [M04](#m04-the-injection-fault-rule), [M05](#m05-check-signs-as-syndrome-bits).

**Conceptual connection.** Connect Gottesman’s parity-check example to the column labels of the 15-to-1 factory.

**Sources.** [Gottesman §3.1](GOTTESMAN_BRIDGE.md#read-the-parts-that-carry-the-argument) · [Factory model](../science/model.md)

### M07 Output parity

**Central question.** Why can two patterns with the same check bits have distinct effects on the output?

**Understanding target.** Track the common output Z factor of each faulty injection and read its parity separately from the four syndrome bits.

**Prerequisites.** [M04](#m04-the-injection-fault-rule), [M06](#m06-binary-check-columns).

**Conceptual connection.** Relate a zero-syndrome, odd-parity pattern to an undetected logical error.

**Sources.** [Gottesman §3.4](GOTTESMAN_BRIDGE.md#read-the-parts-that-carry-the-argument) · [Factory model](../science/model.md)

### M08 The fifteen input labels

**Central question.** Why are there fifteen distinct nonzero slots in the fixed gadget?

**Understanding target.** Identify the fifteen phase-gadget supports via the four check wires and the common output wire. Relate the product of the ideal rotations to the target output state.

**Prerequisites.** [M03](#m03-gate-teleportation), [M06](#m06-binary-check-columns), [M07](#m07-output-parity).

**Conceptual connection.** Explain which parts of the circuit are inherited and which degrees of freedom an input assignment can use.

**Sources.** [Factory model](../science/model.md) · [Related work](../references/RELATED_WORK.md)

### M09 The first undetected slot faults

**Central question.** How many individual slot faults can vanish under the checks?

**Understanding target.** Explain why neither one fault nor a pair of distinct faults has zero syndrome. Characterize an undetected weight-three slot fault by a zero-XOR triple.

**Prerequisites.** [M06](#m06-binary-check-columns), [M07](#m07-output-parity), [M08](#m08-the-fifteen-input-labels).

**Conceptual connection.** Use binary column geometry to derive the leading cubic error for small independent slot noise.

**Sources.** [Factory model](../science/model.md) · [Noise analysis](../science/noise.md)

### M10 Sources and slots

**Central question.** How can three affected states come from just one event?

**Understanding target.** Distinguish the source-burst vector from the fifteen-position raw error mask. Explain how an assignment converts source events into simultaneous slot errors.

**Prerequisites.** [M08](#m08-the-fifteen-input-labels), [M09](#m09-the-first-undetected-slot-faults).

**Conceptual connection.** Interpret fault order relative to the probability of the events being counted, which can differ from the physical error weight.

**Sources.** [Factory model](../science/model.md) · [Routing and decision rules](../science/routing.md)

### M11 Acceptance and error

**Central question.** What statistics describe a postselected factory?

**Understanding target.** Separate acceptance probability, joint probability of accepting a bad output, and error conditioned on acceptance. Under independent retries, convert acceptance into expected raw inputs per success.

**Prerequisites.** [M07](#m07-output-parity), [M10](#m10-sources-and-slots).

**Conceptual connection.** Treat rejection as part of the resource budget even when it improves the fidelity of the states delivered.

**Sources.** [Gottesman §4.6](GOTTESMAN_BRIDGE.md#read-the-parts-that-carry-the-argument) · [Factory model](../science/model.md) · [Routing and decision rules](../science/routing.md)

### M12 The single-block design question

**Central question.** What can input assignment improve if the distillation circuit stays fixed?

**Understanding target.** State the task with five sources, three inputs per source, fifteen fixed slot labels, and four checks. Specify which assumptions make a comparison between two assignments valid.

**Prerequisites.** [M08](#m08-the-fifteen-input-labels), [M09](#m09-the-first-undetected-slot-faults), [M10](#m10-sources-and-slots), [M11](#m11-acceptance-and-error).

**Conceptual connection.** Bring the circuit, source correlations, and acceptance accounting together before changing the layout.

**Sources.** [Factory model](../science/model.md) · [Routing and decision rules](../science/routing.md)

## Phase II. Narrative and innovation

### M13 A bundle induces one check column

**Central question.** How does the factory report one whole-bundle fault?

**Understanding target.** Compute the XOR of the three slot labels assigned to any one source. Assemble the five resulting columns into a source-syndrome map.

**Prerequisites.** [M06](#m06-binary-check-columns), [M10](#m10-sources-and-slots), [M12](#m12-the-single-block-design-question).

**Conceptual connection.** Replace a correlated fifteen-position mask by a five-bit source vector with a derived linear syndrome.

**Sources.** [Routing and decision rules](../science/routing.md)

### M14 An explicit five-source assignment

**Central question.** How can the five source columns be made distinct and nonzero?

**Understanding target.** Verify the five listed triples partition the fifteen labels. Compute 7, 1, 4, 10, and 8 as the corresponding source syndromes in the displayed basis.

**Prerequisites.** [M12](#m12-the-single-block-design-question), [M13](#m13-a-bundle-induces-one-check-column).

**Conceptual connection.** Connect the constructive slot assignment to the abstract design requirement on syndrome columns.

**Sources.** [Routing and decision rules](../science/routing.md)

### M15 Complementary burst histories

**Central question.** Why is every record shared by exactly two source histories in this assignment?

**Understanding target.** Use the zero XOR of all fifteen columns and rule out every proper nonempty zero-XOR subset of the five distinct source columns. Identify the kernel as the all-zero and all-one vectors.

**Prerequisites.** [M13](#m13-a-bundle-induces-one-check-column), [M14](#m14-an-explicit-five-source-assignment).

**Conceptual connection.** Explain why complementing the burst history preserves the record while flipping output parity. Recover the same kernel by imposing equal neighboring burst bits along the path of four comparisons in the five-tie receiver.

**Sources.** [Routing and decision rules](../science/routing.md) · [Phase-tied comparisons](../science/phase-tied-receivers.md#two-string-projections)

### M16 Fifth-order conditional error

**Central question.** What becomes of the accepted output when only zero syndrome is kept?

**Understanding target.** Compute acceptance from the all-zero and all-one source vectors. Divide the bad accepted mass by acceptance and contrast the low-noise order with a layout containing a zero-XOR triple.

**Prerequisites.** [M09](#m09-the-first-undetected-slot-faults), [M11](#m11-acceptance-and-error), [M15](#m15-complementary-burst-histories).

**Conceptual connection.** Relate rejection of all proper nonempty burst subsets to the exact error law, keeping per-source probability separate from per-slot marginal error.

**Sources.** [Routing and decision rules](../science/routing.md)

### M17 Maximum syndrome information

**Central question.** Why can the rank-four record reproduce a decision based on any other whole-burst assignment?

**Understanding target.** Show that another assignment’s syndrome is constant on the same complement pairs. Describe how to recover that syndrome from the rank-four record and reuse the other decision rule.

**Prerequisites.** [M13](#m13-a-bundle-induces-one-check-column), [M15](#m15-complementary-burst-histories).

**Conceptual connection.** Identify the scope of the comparison as the whole-burst model with a fixed circuit and decision rules that use its classical checks.

**Sources.** [Routing and decision rules](../science/routing.md)

### M18 Correction from nonzero records

**Central question.** When can the factory use a nonzero record to keep an output?

**Understanding target.** Compare the two posterior history masses for a given record. Explain the parity correction associated with the more likely history and what can happen when it is wrong.

**Prerequisites.** [M07](#m07-output-parity), [M15](#m15-complementary-burst-histories), [M17](#m17-maximum-syndrome-information).

**Conceptual connection.** Connect the information in the syndrome to a choice between rejection and a classical-frame or physical Pauli correction.

**Sources.** [Routing and decision rules](../science/routing.md)

### M19 The yield and fidelity trade-off

**Central question.** Which syndrome records should be kept first at a given release rate?

**Understanding target.** For identical independent source rates below one half, classify records by smaller burst count 0, 1, or 2. Rank their conditional risks and interpret randomization at the acceptance boundary.

**Prerequisites.** [M11](#m11-acceptance-and-error), [M16](#m16-fifth-order-conditional-error), [M18](#m18-correction-from-nonzero-records).

**Conceptual connection.** Explain why keeping all records with correction and keeping only zero syndrome implement different operating points. Transfer the ordering of the records to a phase-tied receiver and account for the probability of its computational projections.

**Sources.** [Routing and decision rules](../science/routing.md) · [Observed syndrome and yield](../science/phase-tied-receivers.md#observed-syndrome-and-yield)

### M20 Proving what the checks can see

**Central question.** What does a finite pattern check establish about the routing argument?

**Understanding target.** Match the 32 five-bit histories to 16 complementary pairs and classify all accepted masks by parity. Explain why this finite check validates the concrete assignment while the kernel argument proves structural maximality.

**Prerequisites.** [M14](#m14-an-explicit-five-source-assignment), [M15](#m15-complementary-burst-histories), [M17](#m17-maximum-syndrome-information), [M19](#m19-the-yield-and-fidelity-trade-off).

**Conceptual connection.** Connect direct enumeration to the two distinct proof obligations of verifying a construction and comparing it to every layout.

**Sources.** [Routing and decision rules](../science/routing.md) · [Verification](../verification/README.md)

### M21 Partial bursts from one source

**Central question.** Can one affected source hide a fault if some of its states remain good?

**Understanding target.** Prove that no nonempty subset of a noncollinear triple has zero XOR. Explain how a different layout can lose this property.

**Prerequisites.** [M09](#m09-the-first-undetected-slot-faults), [M14](#m14-an-explicit-five-source-assignment), [M16](#m16-fifth-order-conditional-error).

**Conceptual connection.** Extend the single-source check from whole bundles to all possible subsets of one assigned triple.

**Sources.** [Noise analysis](../science/noise.md)

### M22 A whole burst and a partial pair

**Central question.** Can every harmful whole-plus-pair event be removed without giving up the rank-four routing?

**Understanding target.** Identify harmful ordered events by the pair-XOR test. Understand how the parity of the linear-functional counts forces at least one event and how the displayed layout attains one.

**Prerequisites.** [M15](#m15-complementary-burst-histories), [M20](#m20-proving-what-the-checks-can-see), [M21](#m21-partial-bursts-from-one-source).

**Conceptual connection.** Describe which unweighted multiplicity is optimized and how heterogeneous event rates lead to a different design question.

**Sources.** [Noise analysis](../science/noise.md) · [Verification](../verification/README.md)

### M23 Independent errors on top of bursts

**Central question.** How should local slot faults combine with a whole-source fault?

**Understanding target.** Use symmetric difference of fault masks. Show how the same slot can be toggled twice, and distinguish the local rate q from the whole-source rate p.

**Prerequisites.** [M10](#m10-sources-and-slots), [M15](#m15-complementary-burst-histories), [M21](#m21-partial-bursts-from-one-source).

**Conceptual connection.** Connect two independent noise mechanisms to the same syndrome and output parity without treating their events as mutually exclusive.

**Sources.** [Noise analysis](../science/noise.md)

### M24 Exact noise polynomials

**Central question.** How can the acceptance and the accepted parity bias be computed without enumerating all masks?

**Understanding target.** Use binary character orthogonality for the zero-syndrome filter. Explain the eight-slot support of nonzero check characters, the counts of even five-bit characters, and the role of the signed acceptance term.

**Prerequisites.** [M13](#m13-a-bundle-induces-one-check-column), [M15](#m15-complementary-burst-histories), [M23](#m23-independent-errors-on-top-of-bursts).

**Conceptual connection.** Recover conditional infidelity from acceptance and signed mass. Check the pure-burst and pure-local limits against their direct counts.

**Sources.** [Noise analysis](../science/noise.md) · [Verification](../verification/README.md)

### M25 The crossover in suppression order

**Central question.** When do independent slot errors erase the fifth-order behavior in the burst rate?

**Understanding target.** Identify the accepted paths contributing pure cubic local error and mixed terms with one or two source faults. Explain why q must scale at most as p cubed to preserve fifth-order suppression when both rates tend to zero.

**Prerequisites.** [M16](#m16-fifth-order-conditional-error), [M23](#m23-independent-errors-on-top-of-bursts), [M24](#m24-exact-noise-polynomials).

**Conceptual connection.** Connect the leading powers to a quantitative constraint on a routing or storage implementation. In the phase-tied receiver, explain separately why a fixed extraction phase gives an infidelity floor and how an erroneous comparison can accept a rejected burst history.

**Sources.** [Noise analysis](../science/noise.md) · [Scheduling and costs](../science/scheduling.md) · [Deterministic phase mismatch](../science/phase-tied-receivers.md#finite-deterministic-mismatch)

### M26 Scheduling the same circuit

**Central question.** What does it cost to deliver the prescribed source states to their slots?

**Understanding target.** Compare assignments using a common injection schedule. Account for which states have to wait, what is buffered or routed, and how rejection changes cost per output. State the access assumptions behind the comparison.

**Prerequisites.** [M11](#m11-acceptance-and-error), [M16](#m16-fifth-order-conditional-error), [M22](#m22-a-whole-burst-and-a-partial-pair), [M25](#m25-the-crossover-in-suppression-order).

**Conceptual connection.** Relate the single-block design to across-block interleaving using comparable source budgets and availability assumptions.

**Sources.** [Gottesman §4.1](GOTTESMAN_BRIDGE.md#read-the-parts-that-carry-the-argument) · [Scheduling and costs](../science/scheduling.md) · [Related work](../references/RELATED_WORK.md)

### M27 More check wires

**Central question.** What changes when the fifteen-slot circuit is replaced by a larger punctured Reed–Muller gadget?

**Understanding target.** Relate m check bits to the 2^m minus one nonzero labels. Explain how the modulo-eight weights give the required transversal phase and identify the continuing output-parity rule.

**Prerequisites.** [M08](#m08-the-fifteen-input-labels), [M15](#m15-complementary-burst-histories).

**Conceptual connection.** Distinguish enlarging the underlying distillation circuit from changing the input assignment of a fixed circuit.

**Sources.** [Gottesman §4.3](GOTTESMAN_BRIDGE.md#read-the-parts-that-carry-the-argument) · [Larger gadgets](../science/scaling.md)

### M28 Constructing larger source groups

**Central question.** How do odd bundles with a prescribed source syndrome support higher burst order?

**Understanding target.** Reserve independent seed labels and their sum, distribute zero-XOR sets while keeping each bundle odd, and track the all-bundle complement ambiguity. Read the rate and raw-state count together.

**Prerequisites.** [M15](#m15-complementary-burst-histories), [M16](#m16-fifth-order-conditional-error), [M27](#m27-more-check-wires).

**Conceptual connection.** Explain how the source-order law extends without asserting a favorable physical overhead scaling.

**Sources.** [Larger gadgets](../science/scaling.md)

### M29 Evidence and attribution

**Central question.** Which checks support the claims and where do their guarantees end?

**Understanding target.** Distinguish the inherited factory, exact routing proofs, finite enumerations, and scheduling model. In the phase-tied receiver, distinguish the mixed-parity extraction, the measured burst syndrome, and the four-tie lower bound for disjoint supports.

**Prerequisites.** [M20](#m20-proving-what-the-checks-can-see), [M22](#m22-a-whole-burst-and-a-partial-pair), [M24](#m24-exact-noise-polynomials), [M26](#m26-scheduling-the-same-circuit), [M28](#m28-constructing-larger-source-groups).

**Conceptual connection.** Reconcile the noise assumptions, resource accounting, and scope of each result before comparing with related work.

**Sources.** [Scientific account](../science/README.md) · [Four-tie lower bound](../science/phase-tied-receivers.md#four-ties-within-the-disjoint-receiver-family) · [Related work](../references/RELATED_WORK.md) · [Verification](../verification/README.md)

### M30 The complete routing argument

**Central question.** When should a designer expect a better input assignment to help?

**Understanding target.** Tell the story from correlated source outputs and existing checks through the explicit rank-four assignment, its reliability choices, the optimal mixed-event count, the crossover, and the cost of delivery.

**Prerequisites.** [M16](#m16-fifth-order-conditional-error), [M17](#m17-maximum-syndrome-information), [M19](#m19-the-yield-and-fidelity-trade-off), [M22](#m22-a-whole-burst-and-a-partial-pair), [M25](#m25-the-crossover-in-suppression-order), [M26](#m26-scheduling-the-same-circuit), [M28](#m28-constructing-larger-source-groups), [M29](#m29-evidence-and-attribution).

**Conceptual connection.** Tie the source model to the check record and the costs that determine whether improved ideal fidelity produces a useful factory. Explain why a phase-tied parity receiver can have the same syndrome and conditional infidelity while paying a different acceptance cost.

**Sources.** [Scientific account](../science/README.md) · [Routing and decision rules](../science/routing.md) · [Phase-tied receiver](../science/phase-tied-receivers.md) · [Noise analysis](../science/noise.md) · [Scheduling and costs](../science/scheduling.md) · [Larger gadgets](../science/scaling.md)
