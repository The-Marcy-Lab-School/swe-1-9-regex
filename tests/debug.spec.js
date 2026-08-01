const { isValidCompanyUsername } = require('../src/debug');

const testSuiteName = 'Debug Tests';

describe(testSuiteName, () => {
  it('isValidCompanyUsername - correctly checks if an employee has a valid username', () => {
    expect(isValidCompanyUsername('sales9b-ajohnson1', 'albert', 'johnson')).toBe(true);
    expect(isValidCompanyUsername('tech1a-jjones', 'jason', 'jones')).toBe(true);
    expect(isValidCompanyUsername('sales4b-areyes', 'ana', 'reyes')).toBe(true);

    expect(isValidCompanyUsername('areyes', 'ana', 'reyes')).toBe(false);
    expect(isValidCompanyUsername('', 'joe', 'cats')).toBe(false);
  });
});
