# RSpec appendix (optional)

Use when the host project tests with RSpec. The core TDD skill stays framework-agnostic; this file is example-only.

## Good: scenario in structure and assertion

Specification: when a test suite run's status is `passed`, its label says `Passed`.

```ruby
describe "#label" do
  context "when status is 'passed'" do
    it "returns 'Passed'" do
      test_suite_run = TestSuiteRun.new(status: "passed")
      expect(test_suite_run.label).to eq("Passed")
    end
  end
end
```

## Bad: vague correctness

```ruby
describe "#label" do
  it "returns the correct value" do
    test_suite_run = TestSuiteRun.new(status: "passed")
    expect(test_suite_run.label).to eq("Passed")
  end
end
```

The bad example hides the scenario and asserts "correct" instead of naming the expected behavior.
